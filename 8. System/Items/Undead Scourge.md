---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Agile]]", "[[Finesse]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** A character who is a member of the Knights of Lastwall has access to this weapon.

An undead scourge is a *+1 striking vitalizing dagger* with a bluish-white metal blade that emits a faint glow. These used to be weapons of Pharasmin undead slayers only, but the slayers have since shared the secrets of their creation with the Knights of Lastwall.

**Activate—Sever from the Void** `pf2:f` (concentrate, divine, vitality)

**Frequency** once per hour

**Trigger** You hit and damage an undead creature with an undead scourge

**Effect** You disrupt the undead's connection to void energy. For 1 minute, the undead damaged with the dagger can't be healed by void energy unless the effect attempting to heal the undead first counteracts the undead scourge's effect, which has a counteract rank of 4th and a DC of 25. Vitality energy still has the usual effects on the undead.

**Source:** `= this.source` (`= this.source-type`)
