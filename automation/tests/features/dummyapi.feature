""" Created by Pallavi14545 at 8/16/2020   """
Feature: Get list of all users
  As an application I should be able to get a
  list of users

  Scenario: Get list of all users
  Given application requires a list of users
  When  get request is sent to the endpoint
  Then  list of users is returned as a Json response with the HTTP status "200"
