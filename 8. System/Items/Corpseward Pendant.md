---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *corpseward pendant* is usually shaped like the skull of a humanoid or small animal.

**Activate** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You become undetectable to undead creatures for 10 minutes. Undead can't see, hear, or smell you, or detect you with sensory capabilities such as tremorsense. A creature can attempt a DC 18 [[Will]] save saving throw to ignore this effect. If an undead has reason to believe that [[Undetected]] opponents are present, it can still attempt to [[Seek]] or Strike you. If you attempt to use a vitality spell to damage undead, touch or damage an undead creature, or attack any creature while warded in this manner, the pendant's effects immediately end. An undead creature who observes you in this manner or one who succeeds at the Will save is immune to the *corpseward pendant* for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
