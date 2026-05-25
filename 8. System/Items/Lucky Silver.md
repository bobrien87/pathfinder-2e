---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Fortune]]", "[[Magical]]"]
price: "{'gp': 140}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These coins—copper, silver, or gold depending on their potency—were not minted for circulation. Rather, friendly fey helped to create them as wards against the abilities of some gremlins, namely pugwampis. The coins are said to protect the bearer against misfortunes of all stripes, though, not merely those of gremlins and have come to be seen as good luck charms the world over. Each coin, regardless of the metal used to mint it, has a canine face on both sides; on one side, the face's mouth is open in a wide smile, while the other shows the face snarling.

**Activate—Guarded Fortune** `pf2:f` (fortune, manipulate)

**Trigger** You fail a skill check or a saving throw due to a misfortune effect

**Effect** Flip the coin. If it lands on the smiling face, reroll the triggering check; since this activation has the fortune effect, any misfortune effect is canceled out for this check. You must use the new result, even if it's worse. If it lands on the snarling face, nothing happens. Either way, you're temporarily immune to Guarded Fortune for 1 hour.

**Craft Requirements** Any checks made to craft this item while under a misfortune effect are automatic critical failures.

**Source:** `= this.source` (`= this.source-type`)
