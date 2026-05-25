---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Primal]]"]
price: "{'gp': 220}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made of materials scavenged from wild places, a *druid's crown* can be rebuilt for a variety of benefits. The crown grants you a +1 item bonus to a skill, and can be activated to cast a spell, both depending on the material used to build the crown, as listed on the table below. If you invest and wear *living mantle* along with the crown, the crown's item bonus increases by 1 and its spell's DC rises to 27.

You can invest this item only if you're a druid. When you do, as a 10-minute activity that has the manipulate trait, you can disassemble and rebuild the crown with different materials, changing its item bonus and spell accordingly.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The crown casts its spell at 2nd rank (DC 20).

**Craft Requirements** You are a druid.

MaterialItem BonusSpellAntlersIntimidation[[Enlarge]]FlowersDiplomacy[[Animal Allies]]LeavesStealth[[One with Plants]]

**Source:** `= this.source` (`= this.source-type`)
