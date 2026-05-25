---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Divine]]", "[[Holy]]", "[[Shove]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The Empyreal word for "repent" is etched in golden lettering on the shaft of this *+2 greater striking merciful dawnsilver warhammer*. If you are unholy, you are [[Enfeebled]] 2 while carrying or wielding this weapon.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You hold your weapon aloft, calling on righteousness to steel your resolve. You cast protection targeting yourself.

**Redeemer Wielder** If you're a champion with the redemption cause, you also gain the following two benefits.

- When you critically hit an unholy creature with the blessed reformer, until the end of your next turn, the creature takes a –10-foot penalty to its Speeds and can't Step.
- You can Activate the weapon in the following way.

**Activate** `pf2:1` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You hit a creature using the blessed reformer as your last action

**Effect** You cast [[Calm]] at the same rank as your champion focus spells. It must target the creature you hit, and the creature takes a status penalty on its save against the spell equal to the blessed reformer's number of weapon damage dice.

**Craft Requirements** You're a champion with the redemption cause. The initial materials must include 140 gp of dawnsilver.

**Source:** `= this.source` (`= this.source-type`)
