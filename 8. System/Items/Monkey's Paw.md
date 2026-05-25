---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Cursed]]", "[[Magical]]", "[[Misfortune]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This dried, gnarled hand is clenched in a fist, waiting for a creature to pick it up. When you pick up the *monkey's paw*, the hand opens, revealing three withered fingers. The *monkey's paw* grants you three wishes (with the effects of a success on the *wish* ritual), curling one finger after every one. Once you pick up the *monkey's paw*, you cannot discard the hand until it returns to a clenched fist by granting its three wishes. Any attempts to discard the hand, even with the effects of a *wish* ritual, are unsuccessful as the *monkey's paw* reappears among your possessions within 1d4 hours; it doesn't work for any other creature in the intervening time. The hand returns even if another creature steals it from you. Once you make all three wishes, the *monkey's paw* uses [[Interplanar Teleport]] to travel to a random point in the multiverse.

Whenever the *monkey's paw* hears you utter a statement that sounds like a wish, even if you don't use the words "I wish," it activates and grants a twisted, horrifying version of your wish, producing any effect within the possibility of *wish* ritual, and potentially a greater effect at the GM's discretion.

**Source:** `= this.source` (`= this.source-type`)
