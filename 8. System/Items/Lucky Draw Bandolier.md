---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "worn"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This beige bandolier has a rectangular holster, which allows it to contain a standard-sized Harrow deck, and red pockets embroidered with goldwork in a strange but appealing mixture of Alkenstar and Varisian motifs.

**Activate—Secret Ace** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You draw a card from the bandolier and Interact to load the card into a gun or crossbow you're wielding that requires 1 action to reload. The drawn card immediately transforms into magical ammunition with a type depending on the drawn card's suit, and a new copy of that card returns to the deck, ready to be drawn again. When the card transforms into ammunition, it transforms into a firearm round or crossbow bolt appropriate for the weapon you chose to reload, even if magical ammunition of the drawn variety would normally be limited to ammunition of a different type (such as a storm arrow normally only being available in arrow form). Either draw a card from the Harrow deck or roll 1d6 to determine the suit of the card. The result determines the type of magical ammunition the card becomes, as per the table below. Magical ammunition created this way lasts 10 minutes or until you fire it, whichever comes first.

d6Ability (Suit)Ammunition1Strength (Hammer)[[Meteor Shot]]2Dexterity (Key)[[Storm Arrow]]3Constitution (Shield)[[Corrosive Ammunition]]4Intelligence (Book)Explosive shot5Wisdom (Star)[[Fate Shot]]6Charisma (Crown)[[Fairy Bullet]]

**Source:** `= this.source` (`= this.source-type`)
