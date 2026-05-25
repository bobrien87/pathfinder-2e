---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Magical]]"]
price: "{'gp': 32}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Beginner Box"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lustrous, rat-shaped pyrite statuette is 1 inch tall. When activated, the statuette transforms into a flesh-and-blood giant rat. You can use the following action when you hold the *pyrite rat*. You can use this action only once per day, and the rat remains transformed for 1 hour.

**Activate—Transform Statue** `pf2:2` (concentrate, manipulate)

You place the statue on solid ground and speak the rat's secret name, causing the statuette to transform into a living [[Giant Rat]].

In creature form, the giant rat acts on your turn. It gets 2 actions and can't use reactions. You have to spend an action each turn to tell it what to do; otherwise, it tries to run away from danger or cowers where it is.

If the rat is slain while in animal form, it reverts to its statue shape and can't be transformed again until 1 week has passed. If the figurine is destroyed while in its statue form, it's shattered and its magical properties are lost forever.

**Source:** `= this.source` (`= this.source-type`)
