---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 19000}"
usage: "wornheadwear"
bulk: "1"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The traditional headwear for the Red Mantis assassin is the *mask of the mantis*. Most of these masks are constructed from hard leather helmets that serve to obscure the assassin's identity and give them the appearance of possessing a mantis's head. Some variants, however, consist only of the mask itself, and are meant to be worn over the face. Regardless of the shape and style, all masks of the mantis function the same.

Members of the Vernai can use any *mask of the mantis* to enhance their frightening presence—something they often do simply to reveal their standing in the society without speaking a word, as detailed fully in the entry for Vernai's Ire activation below.

While wearing a *mask of the mantis*, you gain a +3 item bonus to Perception checks.

**Activate—Enhance Vision** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast either a 5th-rank [[Darkvision]] or [[See the Unseen]] on yourself.

**Activate—Vernai's Ire** `pf2:1` (concentrate)

**Requirements** You are a member of the Vernai

**Effect** You cause the *mask of the mantis's* eyes to shimmer with crimson light, granting yourself a far more harrowing visage. This light creates illumination equivalent to that of a candle. You can use this ability again to extinguish the frightening glow, but as long as Vernai's Ire remains active, you gain a +3 item bonus to Intimidation checks.

**Activate—Locate Target** 10 minutes (concentrate)

**Frequency** once per day

**Effect** You cast [[Pinpoint]]. If the target of this spell is a creature for which you've accepted a contract to assassinate, you are considered to have seen the creature in person for the purposes of *pinpoint's* requirements.

**Source:** `= this.source` (`= this.source-type`)
