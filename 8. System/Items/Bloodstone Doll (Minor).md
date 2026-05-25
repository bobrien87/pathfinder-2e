---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** R (concentrate, manipulate)

**Trigger** A creature within 60 feet casts a summon spell

**Requirements** You have a free hand.

This small doll has been carved from a fragment of Bloodstone. When you Activate a bloodstone doll in response to another's magic, you Interact to take it in hand and hold it up toward the triggering creature. Attempt a counteract check against the triggering spell with a counteract modifier of +9 and a counteract rank of 2. If the spell would be counteracted, the bloodstone doll instead influences the summoned creature. You gain control of the summoned creature and can dictate its 2 actions for that turn. The triggering creature then regains control of their summoned creature, but the summoned creature takes a –2 status penalty to attack rolls against you. Your bloodstone doll shatters when the summon spell ends

**Craft Requirements** You have a fragment of the Bloodstone at the heart of the Bloodstone Conservatory.

**Source:** `= this.source` (`= this.source-type`)
