---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Backswing]]", "[[Finesse]]", "[[Reach]]", "[[Sweep]]", "[[Versatile b]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Traditionally a favored weapon in Molthune for settling disputes between military leaders, the dancer's spear has seen a recent resurgence in popularity in the neighboring kingdom of Nirmathas, largely due to its effectiveness at striking down attacking skeletons and other undead from a relatively safe distance. A dancer's spear has a 7-foot-long wooden haft capped with a triangular metal blade at one end, counterbalanced on the other end with a reinforced metal sleeve that, in a pinch, can be used as an effective striking surface.

**Source:** `= this.source` (`= this.source-type`)
