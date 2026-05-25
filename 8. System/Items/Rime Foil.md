---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Deadly d8]]", "[[Disarm]]", "[[Finesse]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The steely blue blade of this *+2 striking frost rapier* emerges from a hilt wrapped in thick leather and trimmed in fur to protect the wielder's hand.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You hit a creature using the *rime foil* as your last action

**Effect** You cast 5th-rank [[Phantom Prison]] on the target (DC 22 [[Will]] save to disbelieve). If the target has been damaged by a *shattered plan* in the last round, the DC is instead DC 24 [[Will]] save.

**Special** The rime foil pairs with the *[[Shattered Plan]]*.

**Source:** `= this.source` (`= this.source-type`)
