def prompt_inputs():
    vals = {}
    
    vals["adj1"] = input("Give me an adjective: ")
    vals["noun1"] = input("Give me a noun: ")
    vals["verb_past1"] = input("Give me a verb, past tense: ")
    vals["adverb1"] = input("Give me an adverb: ")
    vals["adj2"] = input("Give me an adjective: ")
    vals["noun2"] = input("Give me a noun: ")
    vals["noun3"] = input("Give me a noun: ")
    vals["adj3"] = input("Give me an adjective: ")
    vals["verb1"] = input("Give me a verb: ")
    vals["adverb2"] = input("Give me an adverb: ")
    vals["verb_past2"] = input("Give me a verb, past tense: ")
    vals["adj4"] = input("Give me an adjective: ")

    return vals

def build_mad_lib(vals):

    outline = "Today I went to the zoo. I saw a adj1 noun1 jumping up and down in its tree. He verb_past1 adverb1 through the large tunnel that led to its adj2 noun2. I got some peanuts and passed them through the age to a gigantic gray noun3 towering above my head. Feeding that animal made me hungry. I went to get a adj3 scoop of ice cream. It filled my stomach. Afterwards I had to verb1 adverb2 to catch our bus. When I got home I verb_past2 my mom for a adj4 day at the zoo."
    outline = outline.replace("adj1", vals["adj1"])
    outline = outline.replace("adj2", vals["adj2"])
    outline = outline.replace("adj3", vals["adj3"])
    outline = outline.replace("adj4", vals["adj4"])
    outline = outline.replace("noun1", vals["noun1"])
    outline = outline.replace("noun2", vals["noun2"])
    outline = outline.replace("noun3", vals["noun3"])
    outline = outline.replace("verb_past1", vals["verb_past1"])
    outline = outline.replace("verb_past2", vals["verb_past2"])
    outline = outline.replace("adverb1", vals["adverb1"])
    outline = outline.replace("adverb2", vals["adverb2"])
    outline = outline.replace("verb1", vals["verb1"])
    
    print(outline)
    
def main():
    build_mad_lib(prompt_inputs())

main()
