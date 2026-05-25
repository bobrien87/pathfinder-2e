---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Disarm]]", "[[Grapple]]", "[[Parry]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *scizore of the crab* is a *+1 scizore* that has the grapple trait in addition to its normal weapon traits.

**Activate** `pf2:1` (manipulate)

**Requirements** Your last action was a successful Strike with this weapon, or you have a creature [[Grabbed]] with this weapon

**Effect** The target is grabbed until the end of your next turn. A grabbed creature can use the [[Escape]] action to get out of the Grab, and the Grab ends for a grabbed creature if you move away from it. This functions as the Grab creature ability.

**Activate** `pf2:1` (manipulate)

**Frequency** once per round

**Requirements** You have a creature grabbed with this weapon

**Effect** The crab claw animates and pinches open and shut, dealing slashing damage equal to the *scizore of the crab*'s number of damage dice.

**Craft Requirements** The initial raw materials must include a claw from a giant crab or similar creature.

**Source:** `= this.source` (`= this.source-type`)
