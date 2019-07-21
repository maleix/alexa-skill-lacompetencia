# Alexa Skill: La Competència

This project is an audio player skill to listen podcasts from 'La Competència' for Amazon Alexa.

[La Competència](https://www.rac1.cat/programes/la-competencia) is a humorous radio program broadcast by the catalan radio company RAC1.

This code uses Python, Flask and [Flask-Ask](https://github.com/johnwheeler/flask-ask).

## Languages

It only supports spanish language.

## Usage

By default, when skill is opened it will play the last available podcast, e.g.:

`alexa, pon la competencia`

You can also ask for a podcast of the last 7 days, e.g.:

`alexa, abre la competencia y pon la del martes`

To see a more extensive list of what you can say, read [SampleUtterances](SampleUtterances.md)

## Execution

```python
# Install dependencies
pip install -r requirements.txt

# Execute main class
python src/server.py
```
