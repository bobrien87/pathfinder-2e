---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Talisman]]", "[[Visual]]"]
price: "{'gp': 130}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (concentrate)

**Prerequisites** You are a master in Deception

This rough wooden coin hangs from a string drilled through a hole at its center. When you Activate the *wooden nickel*, for 10 minutes, you can cause any object you touch of 2 Bulk or less to look, feel, and smell like valuables of a similar size crafted from a precious metal of your choice.

A creature that touches or Interacts with an affected object can attempt a [[Perception]] check against your Deception DC to disbelieve the illusion, and a successful check against your Deception DC with [[Crafting]] check or an appropriate Lore skill will also reveal the item's true nature. After 10 minutes have elapsed since you Activated the *wooden nickel*, all affected objects revert to their true form.

**Source:** `= this.source` (`= this.source-type`)
