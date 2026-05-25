---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Healing]]", "[[Invested]]", "[[Magical]]", "[[Vitality]]"]
price: "{'gp': 250}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Stories tell of a forgotten king who once loved his subjects so much he was willing to give his own life energy for them, using an object like the *crown of the companion*. Whether true or not, this majestic wooden crown bears elaborate carvings depicting that tale with images of a regal figure giving more and more of themself to a throng of needy subjects. While wearing this crown, you gain a +1 item bonus to Diplomacy checks.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You bow to an ally within 30 feet, creating a magical bond between the two of you as if you cast [[Share Life]] targeting the ally. The link remains even if you move more than 30 feet away from them. At the end of the spell's duration, your ally recovers 4d8 healing Hit Points and you recover half of what they recover.

**Source:** `= this.source` (`= this.source-type`)
