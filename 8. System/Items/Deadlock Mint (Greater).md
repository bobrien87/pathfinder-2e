---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 110}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

*Deadlock mint* is a species of mint with small, green flowers, said to grow on battlefields where the opposing sides were equally matched. Sprigs of the flowers blow gently in a breeze of their own creation. If you cast [[Mystic Armor]] using *deadlock mint*, you release a small blast of concussive air in an emanation of a size that depends on the catalyst's type. Unattended objects up to a certain Bulk limit are pushed away from you. Large or smaller creatures must succeed at a Fortitude save equal to your spell save DC or be pushed the same distance away from you.

Objects of 1 Bulk or less and creatures that fail the save are pushed 10 feet. Objects of up to 2 Bulk are pushed 5 feet, and Huge creatures must succeed at the save or be pushed 5 feet.

**Source:** `= this.source` (`= this.source-type`)
