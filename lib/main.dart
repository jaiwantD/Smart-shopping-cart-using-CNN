

/*

      __          _________          _       _       _______
      | |   /\    |_   _|\ \        / //\    | \ | ||__   __|
      | |  /  \     | |   \ \  /\  / //  \   |  \| |   | |   
  _   | | / /\ \    | |    \ \/  \/ // /\ \  | . ` |   | |   
 | |__| |/ ____ \  _| |_    \  /\  // ____ \ | |\  |   | |   
  \____//_/    \_\|_____|    \/  \//_/    \_\|_| \_|   |_|   
                                                          

*/





import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Shopping Cart',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: WelcomeScreen(),
    );
  }
}

// Welcome screen
class WelcomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Welcome to Shopping'),
        backgroundColor: const Color.fromARGB(255, 44, 28, 133),
        foregroundColor: Colors.white,
      ),
      body: Container(
        width:500,
        height:1000,
        color:Colors.white,
        child: Center(
          child: ElevatedButton(
            onPressed: () {
              // Navigate to user details screen
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => UserDetailsScreen()),
              );
            },
            style: TextButton.styleFrom(
            backgroundColor: Colors.blue,
            foregroundColor: Colors.white,
          ),
            child: Text('Press here to start shopping'),
          ),
        ),
      ),
    );
  }
}

// User details screen
class UserDetailsScreen extends StatefulWidget {
  @override
  _UserDetailsScreenState createState() => _UserDetailsScreenState();
}

class _UserDetailsScreenState extends State<UserDetailsScreen> {
  final _nameController = TextEditingController();
  final _placeController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Enter User Details'),
        backgroundColor: const Color.fromARGB(255, 44, 28, 133),
        foregroundColor: Colors.white,
      ),
      body: Container(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              TextField(
                controller: _nameController,
                decoration: InputDecoration(
                  labelText: 'Enter your name',
                ),
              ),
              TextField(
                controller: _placeController,
                decoration: InputDecoration(
                  labelText: 'Enter your place',
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // Navigate to the shopping cart screen (HomePage)
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => HomePage()),
                  );
                },
                style: TextButton.styleFrom(
            backgroundColor:  const Color.fromARGB(255, 44, 28, 133),
            foregroundColor: Colors.white,
          ),
                child: Text('Login'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    _placeController.dispose();
    super.dispose();
  }
}

// Shopping cart screen (your original app)
class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String? _responseMessage;
  List<dynamic> _items = [];
  double _totalAmount = 0.0;

  Future<void> _processBilling() async {
    final response = await http.post(
      Uri.parse('http://192.168.147.237:5000/process_billing'),
    );

    if (response.statusCode == 200) {
      final jsonResponse = jsonDecode(response.body);
      setState(() {
        _items = jsonResponse['items'];
        _totalAmount = jsonResponse['total_amount'];
        _responseMessage = 'Billing Summary:';
      });
    } else {
      setState(() {
        _responseMessage = 'Error: Unable to process billing';
      }
    ); 
    }
  }

  Future<void> _newUser() async {
    final response = await http.post(
      Uri.parse('http://192.168.147.237:5000/new_user'),
    );

    if (response.statusCode == 200) {
      setState(() {
        _responseMessage = 'New user created. All previous images flushed.';
      });
    } else {
      setState(() {
        _items = [];
        _totalAmount = 0.0; // Reset
        _responseMessage = 'Welcome to Smart Shopping!';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
        backgroundColor: const Color.fromARGB(255, 44, 28, 133),
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              Image.asset('assets/unnamed.png'),   //Image path
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _processBilling,
                child: Text('Proceed to Billing'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _newUser,
                child: Text('new_user_button'),
              ),
              SizedBox(height: 20),
              if (_responseMessage != null) Text(_responseMessage!),
              if (_items.isNotEmpty)
                Column(
                  children: _items.map((item) {
                    return Text('${item['name']}: Rs.${item['price']}');
                  }).toList(),
                ),
              if (_totalAmount > 0)
                Text('Total Amount: Rs.$_totalAmount'),
            ],
          ),
        ),
      ),
    );
  }
}





