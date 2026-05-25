---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Magical]]", "[[Monk]]", "[[Parry]]", "[[Twin]]", "[[Versatile p]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This set of *+2 greater striking flaming feng huo lun* is warm to the touch and wreathed in the bright red and orange glow of a constantly flickering flame. While wielded, you gain cold resistance 2, and you treat the effects of environmental cold as one degree lower. Heavenly rolling flames can be Activated only if you wield two of them, and Activating them counts against the frequency for both weapons.

**Activate—Rolling Flight** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You attach the wheels to your feet, and their constant movement and energy allow you to move through the air. You gain a fly Speed of 20 feet for 10 minutes. While in use in this way, you can't wield the wheels as weapons. You can spend an Interact action at any time to end this effect and re-grip the heavenly rolling flames. If you lack enough free hands to wield them, you drop them in your space.

> [!danger] Effect: Rolling Flight

**Activate—Speed of Heaven** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You cast [[Haste]] as a 3rd-rank occult spell, but you can target only yourself.

**Source:** `= this.source` (`= this.source-type`)
