---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Shield throw 30]]"]
price: "{'gp': 2650}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Shield throw 30 ft.

This standard-grade duskwood meteor shield (Hardness 11, HP 80, BT 40) is a wheel from a ship. While wielding the shield, you gain a +2 item bonus to Sailing Lore and to Athletics checks to Swim.

**Activate** `pf2:2` command

**Frequency** once per day

**Requirements** You're in a body of water

**Effect** For 10 minutes, you don't sink if you haven't succeeded at a Swim action on a turn, and if you're submerged, you automatically ascend 10 feet at the end of your turn. When you Activate the shield, it casts [[Water Walk]] on you. and you can breathe underwater for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
