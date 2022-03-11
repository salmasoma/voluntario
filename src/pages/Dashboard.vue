<script setup lang="ts">
import '../style.css'
</script>
<template>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" type="text/css" href="/static/styles/style.css">
</head>

<body>
    <div class="container">
        <div class="navigation">
            <ul>
                <li>
                    <a href="#">
                        <span class="title" style="font-size: 1.5em;font-weight: 500; margin-left: 10px;;">Voluntario</span>
                    </a>
                </li>
                <li class="hovered">
                    <a href="#">
                        <span class="icon"><ion-icon name="home-outline"></ion-icon></span>
                        <span class="title">Dashboard</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><ion-icon name="notifications-outline"></ion-icon></span>
                        <span class="title">Notifications</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><ion-icon name="help-outline"></ion-icon></span>
                        <span class="title">Help</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><ion-icon name="settings-outline"></ion-icon></span>
                        <span class="title">Settings</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><ion-icon name="log-out-outline"></ion-icon></span>
                        <span class="title">Sign Out</span>
                    </a>
                </li>
            </ul>
        </div>

        <!-- main -->
        <div class="main">
            <div class="topbar">
                <div class="toggle">
                    <ion-icon name="menu-outline"></ion-icon>
                </div>
                <!-- search -->
                <div class="search">
                    <label>
						<input type="text" placeholder="Search here">
						<ion-icon name="search-outline"></ion-icon>
					</label>
                </div>
                <!-- userImg -->
                <div class="user">
                    <ion-icon name="person" style="padding-top: 5px;"></ion-icon>
                </div>
            </div>

            <!-- cards -->
            <div class="cardBox">
                <div class="card">
                    <div>
                        <div class="numbers">82</div>
                        <div class="cardName">Hours Donated</div>
                    </div>
                    <div class="iconBx">
                        <ion-icon name="time"></ion-icon>
                    </div>
                </div>
                <div class="card">
                    <div>
                        <div class="numbers">events</div>
                        <div class="cardName">Events Completed</div>
                    </div>
                    <div class="iconBx">
                        <ion-icon name="list"></ion-icon>
                    </div>
                </div>
                <div class="card">
                    <div>
                        <div class="numbers">13</div>
                        <div class="cardName">Review</div>
                    </div>
                    <div class="iconBx">
                        <ion-icon name="chatbubbles-outline"></ion-icon>
                    </div>
                </div>
                <div class="card">
                    <div>
                        <div class="numbers">4.75</div>
                        <div class="cardName">Rating</div>
                    </div>
                    <div class="iconBx">
                        <ion-icon name="star"></ion-icon>
                    </div>
                </div>
            </div>


            <!-- Add Charts -->
            <div class="graphBox">
                <div class="box">
                    <canvas id="myChart"></canvas>
                </div>
                <div class="box">
                    <canvas id="hours"></canvas>
                </div>
            </div>

            <div class="details">
                <!-- order details list -->
                <div class="recentEvents">
                    <div class="cardHeader">
                        <h2>Recent Events</h2>
                        <a href="#" class="btn">View All</a>
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <td>Name</td>
                                <td>Hours</td>
                                <td>Status</td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Street Cleaning</td>
                                <td>6</td>
                                <td><span class="status inprogress">In Progress</span></td>
                            </tr>
                            <tr>
                                <td>Dog Walking</td>
                                <td>3</td>
                                <td><span class="status pending">Pending</span></td>
                            </tr>
                            <tr>
                                <td>Food Bank</td>
                                <td>4</td>
                                <td><span class="status completed">Completed</span></td>
                            </tr>
                            <tr>
                                <td>Handing Flyers</td>
                                <td>1</td>
                                <td><span class="status absent">Absent</span></td>
                            </tr>
                            <tr>
                                <td>Book Reading</td>
                                <td>3</td>
                                <td><span class="status completed">Completed</span></td>
                            </tr>
                            <tr>
                                <td>Animal Shelter</td>
                                <td>4</td>
                                <td><span class="status completed">Completed</span></td>
                            </tr>
                            <tr>
                                <td>Clothes Donations</td>
                                <td>2</td>
                                <td><span class="status absent">Absent</span></td>
                            </tr>
                            <tr>
                                <td>Street Cleaning</td>
                                <td>2</td>
                                <td><span class="status completed">Completed</span></td>
                            </tr>

                        </tbody>
                    </table>
                </div>




            </div>

        </div>
    </div>


</body>
</template>