---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Extradimensional]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "wornbackpack"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *alchemist's haversack* is a sturdy leather backpack with two compartments. The main section contains an extradimensional space equivalent to a spacious pouch type II, perfect for carrying bulkier alchemist equipment. A secondary partition can hold 2 Bulk of items, 1 of which doesn't count against your Bulk limit. This second compartment can also be activated (see below).

Two shoulder straps and a thick belt for the waist hold the haversack on the wearer securely. These straps have pouches and loops for keeping alchemical items handy. They also contain magically expanded alchemist's toolkit that grants you a +2 item bonus to Crafting checks to create alchemical items.

Water and undesirable material can't seep into the haversack, which cleans itself once per hour. When you reach in any part of the haversack, the item you sought is the first one you find. Also, the haversack preserves mundane ingredients, food, and drink inside, so they stay fresh indefinitely. This feature doesn't prolong the duration of magic or alchemical items.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** You can create versatile vials

**Effect** You pull a versatile vial from the satchel's secondary compartment. It's as effective as the vials you create at the start of the day, not limited like ones created using Quick Alchemy.

**Craft Requirements** You are an alchemist.

**Source:** `= this.source` (`= this.source-type`)
