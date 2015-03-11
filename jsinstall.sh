REQUIREMENTS_FILE="js-requirements.txt"
while read line; do
  echo "Installing from $line"
  git clone $line.git ./static/js/lib/${line##*/} > /dev/null
  echo "Finished installing $line"
done < "$REQUIREMENTS_FILE"
echo "Installation complete"
