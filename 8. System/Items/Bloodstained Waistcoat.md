---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 85}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This white vest has a large crimson bloodstain that can never be removed. Imbued with the anguish of a comrade who bled to death in the creator's arms, a bloodstained waistcoat helps prevent you and your fellow soldiers from suffering the same fate. Your flat check to remove persistent bleed damage is DC 10 instead of DC 15, which is reduced to DC 5 if another creature uses a particularly appropriate action to help.

**Activate—Staunch Bleeding** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The stain on the bloodstained waistcoat gets slightly larger as you bleed in lieu of an ally. The waistcoat ends a persistent bleed condition for one ally within 30 feet, but you gain that condition with the same parameters.

*PFS Note:* This item's change to DCs overwrites any other changes to flat checks, whether beneficial or harmful to the wearer.

**Source:** `= this.source` (`= this.source-type`)
