---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]"]
price: "{'gp': 1400}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Champions adorn these bracers with the symbol of their deity or the text of the tenets they follow. While they're clasped around your forearms, reassuring focus and devotion flow into you through them. Each time you spend a Focus Point to cast a devotion spell, your [[Blessing of the Devoted]] gains a benefit until the start of your next turn, depending on its type.

- **[[Blessed Armament]]** The bracers hold your weapon in place. You gain a +2 item bonus against attempts to [[Disarm]] you of your blessed armament.
- **[[Blessed Shield]]** While raised, the shield grants you resistance 10 to unholy if you're holy, resistance 10 to holy if you're unholy, or resistance 5 to holy and unholy if you're neither.
- **[[Blessed Swiftness]]** The bonus to Speed is +10 feet.

> [!danger] Effect: Bracers of Devotion

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a champion devotion spell. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a champion.

**Source:** `= this.source` (`= this.source-type`)
