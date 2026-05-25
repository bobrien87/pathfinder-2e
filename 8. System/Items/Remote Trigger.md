---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]"]
price: "{'gp': 125}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This trigger array uses percussive alchemical caps and crystals to remotely detonate alchemical bombs through harmonic vibrations. You can Interact to flip up a switch on the trigger, causing it to emit infrasonic pulses that attune it to one alchemical bomb over the course of 10 minutes. The trigger can be attuned to up to three bombs at a time.

**Activate** `pf2:1` (manipulate)

The trigger detonates any number of attuned bombs within 60 feet of it. You choose which ones to detonate. A bomb detonated by remote trigger deals its splash damage to any creature in its square.

**Source:** `= this.source` (`= this.source-type`)
