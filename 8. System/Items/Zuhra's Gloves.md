---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]", "[[Metal]]"]
price: "{'gp': 3000}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elaborate metallic webbing feels soft when wrapped around your hands and forearms. It constantly shifts its strands and connections. The name of a zuhra shuyookh is etched in Talican on the only part of the item that's unchanging. You gain a +3 item bonus to your Reflex DC against attempts to [[Disarm]] an item you're holding in your hands.

**Activate—Zuhra's Stratagem** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** You're wielding a weapon made primarily of metal

**Effect** You extend the weapon and call out the zuhra's name. They channel their magic through the gloves to assist you with their choice of offense or defense (as determined by the GM). The zuhra makes any choices for the spell, and any save DC is 30.

- **Offense** The metal of the gloves wraps around your weapon and channels the zuhra's magic to cast a 6th-rank [[Weapon Storm]] spell, replicating the metal weapon.

- **Defense** The metal flows off your arms, creating a [[Wall of Metal]]. The wall's surface has the same pattern as the gloves. You lose the gloves' item bonus until the barrier ends, at which point the metal returns to your hands and forearms. You can Dismiss the activation.

**Source:** `= this.source` (`= this.source-type`)
