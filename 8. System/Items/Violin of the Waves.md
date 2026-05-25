---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This violin is crafted from finely wrought rosewood that emits a strong, but pleasant, smell of salt water and ocean life. It's engraved with images of sailors working and waves gently rolling. When you make a Performance check using the *violin of the waves*, you gain a +2 item bonus to the check. This bonus increases to +3 if the performer is currently aboard a ship, walking on the ocean, or otherwise immediately adjacent to ocean water.

The violin was created to play a specific tune, one that springs instantly into the mind of anyone who so much as casually strums the instrument. It's a tune of calm waters and safety, but also of pranks played upon shipmates and revelry.

**Activate** 5 minutes (manipulate)

**Frequency** once per day

**Requirements** You must be aboard a ship

**Effect** You play the song. Once it's completed, the weather immediately calms to the normal as it would for the season, as [[Control Weather]]. For the next day, the weather remains in this state, unless affected by other magical effects. Anyone aboard the ship finds their mind wanders when performing tasks however, daydreaming of drunken revelry or other forms of entertainment, and the crew of the ship takes a –2 status penalty to skill checks to do anything other than participate in such revelry.

**Source:** `= this.source` (`= this.source-type`)
