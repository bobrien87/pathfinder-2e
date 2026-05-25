---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 425}"
usage: "worncloak"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long hide cloak is stitched with patches of the ebony hair of a tikbalang. While wearing this cloak, you take a –2 item penalty to saves against illusions but gain a +2 item bonus to Deception checks.

**Activate—Illusory Thrash** `pf2:2` (concentrate, illusion, manipulate, mental)

**Frequency** once per day

**Effect** You wrap the mantle around your body, causing you to briefly appear much larger than you are. Make a melee Strike. This Strike deals an additional 4d6 mental damage.

**Craft Requirements** The initial raw materials must include the hide of a tikbalang.

**Source:** `= this.source` (`= this.source-type`)
