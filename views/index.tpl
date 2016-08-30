<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Fish Food App</title>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.3/css/bootstrap.min.css" integrity="sha384-MIwDKRSSImVFAZCVLtU0LMDdON6KVCrZHyVQQj6e8wIEJkW4tvwqXrbMIya1vriY" crossorigin="anonymous">
  </head>

<div class="container">
  <body>
    <h1>মাছের খাবারের ক্যালকুলেটর</h1>

<form method="POST" action="/result">

  <div class="form-group row">
    <label for="exampleSelect1" class="col-sm-2 col-form-label">কোন প্রকার মাছ?</label>
    <select class="form-control form-control-lg" name="dropdownform">
      <option value="1">ভিয়েতনামী কই</option>
      <option value="2">মনোসেক্স তেলাপিয়া</option>
      <option value="3">মৃগেল</option>
      <option value="3">বাটা</option>
      <option value="3">রুই</option>
      <option value="3">কাতলা</option>
      <option value="3">গ্রাস কার্প</option>
      <option value="3">বিগ হেড কার্প</option>
      <option value="3">থাই পুটি</option>
      <option value="3">কালিবাউস</option>
      <option value="3">সিলভার</option>
      <option value="4">গলদা চিংড়ি</option>
      <option value="5">বাগদা চিংড়ি</option>
      <option value="6">পাঙ্গাস</option>
      <option value="7">মাগুর</option>
    </select>
  </div>


  <div class="form-group row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">প্রতি কেজিতে মাছের সংখ্যা</label>
    <div class="col-sm-10">
      <input type="number" class="form-control form-control-lg" id="inputEmail3" name="TotalFish" placeholder="প্রতি কেজিতে মাছের সংখ্যা">
    </div>
  </div>
  <div class="form-group row">
    <label for="inputPassword3" class="col-sm-2 col-form-label">পুকুরে ছাড়া মোট মাছের সংখ্যা</label>
    <div class="col-sm-10">
      <input type="number" class="form-control form-control-lg" id="inputPassword3" name="FishRange" placeholder="পুকুরে ছাড়া মোট মাছের সংখ্যা">
    </div>
  </div>

  <button type="submit" class="btn btn-primary btn-lg">হিসাব দেখাও</button>
</form>
  
    
  </body>
</div>
</html>
