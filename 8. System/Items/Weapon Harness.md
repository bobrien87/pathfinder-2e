---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Adjustment]]"]
price: "{'gp': 6}"
usage: "applied-to-armor"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A suit of armor with this adjustment incorporates short, flexible harnesses meant to connect weapons to each of its vambraces. These harnesses can each be connected to a melee weapon of light Bulk or less. Attaching or removing a weapon takes an Interact action. Someone else can attach or remove a weapon if you're willing to let them or you're unable to act. You must remove a weapon from its mount before you can completely Release or otherwise stow it.

You gain a +1 circumstance bonus to your Reflex DC against attempts to [[Disarm]] you of a weapon connected to the armor. If the weapon would be knocked from your grasp or you would drop it, the weapon dangles from the bracer by its harness rather than falling to the ground. You can regain control of the weapon in the normal time it takes you to draw it. Attaching a weapon to a weapon harness prevents you from throwing it or using other abilities that would require it to leave your person.

**Source:** `= this.source` (`= this.source-type`)
