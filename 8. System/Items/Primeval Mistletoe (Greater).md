---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3900}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sprig of berry-festooned holly and mistletoe doesn't wilt or rot. It can be used as a primal locus, and it grants a +2 item bonus to Nature checks while you wear it.

**Activate—Anoint** `pf2:2` (manipulate)

**Frequency** once per 10 minutes

**Effect** You squeeze juice from one of the berries and smear it onto a weapon made primarily of wood to cast a 6th-rank [[Runic Weapon]] on it, or onto a creature to cast a 6th-rank [[Runic Body]] on it.

**Activate—Bind** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You touch the sprig, then a tree to cast [[One with Plants]] upon yourself, turning into a vine on the touched tree.

**Activate—Cultivate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You plant the *greater primeval mistletoe* into an area of natural earth or stone. Once planted, the plant immediately sprouts into an area of holly bushes that don't impede movement and that pulse with vitality energy, replicating the effects of a [[Field of Life]] spell. You can Sustain the activation up to 1 minute. When this magic ends, the holly bushes revert back into the original *greater primeval mistletoe*.

**Source:** `= this.source` (`= this.source-type`)
