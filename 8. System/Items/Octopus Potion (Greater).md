---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]", "[[Morph]]", "[[Potion]]", "[[Water]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Eight flailing octopus arms covered in suckers pop out from the sides of your body when you imbibe this potion. The arms share your multiple attack penalty and attempt to [[Grapple]] a random enemy within 15 feet of you. On a success, roll `r 1d4 #Added Effect` to determine an additional effect of the arms, which lasts as long as the target remains [[Grabbed]] or [[Restrained]] by the arms. On subsequent turns, you can use a single action, which has the attack trait, to have the arms either Grapple a creature currently grabbed or restrained (with no added effect) or release any creature they currently hold and repeat their initial effect. After 1 minute, the arms disappear and the potion's effects end.

The Athletics modifier is +22 and the Escape DC is 30.

`r 1d4`Added Effect1The arms cover the eyes; the target is also [[Blinded]].2The arms cover the mouth; the target can't speak.3The arms wrap around the limbs; the flat check for the target to use a manipulate action while grabbed is DC 7 flat check instead of DC 5.4The arms crush your enemy; the target takes bludgeoning damage equal to the potion's level immediately and at the end of each of its turns.

**Source:** `= this.source` (`= this.source-type`)
