---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A lesser variant of the [[Serum of Sex Shift]] with some interesting quirks, a potion of passing fancy is a staple of Arshean artisans, and most temples keep at least a few doses at hand. Upon drinking the potion, your appearance changes, taking on different sex characteristics in line with another gender expression. You have little control over the details of the change, but it lines up with your deepest heartfelt ideal. More importantly, unlike the *serum of sex shift*, a potion of passing fancy doesn't impart the "family resemblance" effect; thus, a drinker too shy or afraid of being recognized to publicly express another gender as themself can experience the change more anonymously.

A *potion of passing fancy's* effects last for 1 hour before slowly fading over 10 minutes; drinking another before the effect fully ends resets its duration and undoes any fading. If you extend the effect this way a fourth consecutive time, your actual form stabilizes with your current characteristics while retaining a "family resemblance" to your original form, as per the effects of a single *serum of sex shift*.

**Source:** `= this.source` (`= this.source-type`)
