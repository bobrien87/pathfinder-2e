---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Divine]]", "[[Invested]]", "[[Light]]"]
price: "{'gp': 650}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

If you worship a deity, this golden amulet transforms into your deity's religious symbol when you invest it. You gain a +2 item bonus to Religion. The symbol casts dim light in a @Template[emanation|distance:20].

**Activate—Spiritual Light** `pf2:2` (concentrate, light, revelation)

**Frequency** once per day

**Effect** The light cast by the symbol becomes bright light for 10 minutes and shines through bodies to reveal hints of the spirits within. Creatures in the light receive a –2 status penalty to Deception and Stealth checks, and while it's active your enemies in the light gain weakness 5 to spirit damage.

You can Dismiss this activation.

> [!danger] Effect: Aura: Shining Symbol

**Craft Requirements** You must be holy or unholy.

**Source:** `= this.source` (`= this.source-type`)
