---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Disarm]]", "[[Grapple]]", "[[Magical]]", "[[Thrown 20]]"]
price: "{'gp': 275}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The tiger fork is a *+1 trident* with the disarm and grapple traits. It has wide, flaring prongs that can be used to fend off deadly beasts and entrap opponents during combat. While you have another creature Grabbed with the *tiger fork*, you gain a +1 circumstance bonus to saves against forced movement effects.

**Activate—Fork Grip** `pf2:1` (manipulate)

**Requirements** Your last action was a successful Strike against a creature

**Effect** You can activate the *tiger fork* to attempt to [[Grapple]] the creature. This attempt uses the same multiple attack penalty as the required Strike.

**Source:** `= this.source` (`= this.source-type`)
