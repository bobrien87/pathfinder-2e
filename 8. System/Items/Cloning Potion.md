---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 5000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you drink a cloning potion, you split in two, one version of you remaining in your space and the other moving into an adjacent space. Your clone, which has the minion trait, looks like you and remains for 1 minute. Provided you are both on the same plane, you can command your clone telepathically with a single action with the concentrate trait. You can also issue verbal commands, as normal for a minion. As an action that has the concentrate trait, you can sense through your clone. When you do, you lose all sensory information from your own body. You can Dismiss this sense-sharing effect.

You and your clone share Hit Points, and the clone uses your statistics. Spells and effects target you and your clone as if you are separate creatures. The clone can Activate your abilities and Cast your Spells, limited by its number of actions, but you share elements such as use limits, frequency, and spell slots. In other words, your clone using one of your resources works as if you did so in or from your clone's space. Your clone has gear identical to your own, excepting artifacts and consumables. Any item taken from the clone melts into silvery dust within seconds, with ammunition or thrown objects lasting just long enough to travel to and possibly hit their target.

When the duration lapses, your clone melts into silvery dust. You become temporarily immune to cloning potion for 1d4 days.

**Source:** `= this.source` (`= this.source-type`)
