---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

In many parts of Tian Xia, it's tradition to mint coins with holes in the centers for the purpose of being able to thread a cord through them and tie them off for security and ease of transaction. This immaculately braided red cord is made in this tradition and can hold up to 100 coins at any given time. As long as you carry a fortune cord, you gain a +2 item bonus to skill checks to [[Earn Income]]. If you load up to 100 coins onto a fortune cord as part of your daily preparations, you can Activate the magic item in two different ways until the next time you make your daily preparations, provided all the loaded coins are of the same type.

**Activate—Merchant's Bludgeon** `pf2:1` (concentrate)

**Frequency** once per day

**Requirements** You have at least 50 coins loaded onto the fortune cord

**Effect** You transform the fortune cord into a *+2 striking nunchaku* for 1 minute. The type of coin loaded onto the cord determines the additional weapon property rune that manifests on this *+2 striking nunchaku*, as follows.

- **Copper**: [[Corrosive]]

- **Silver**: [[Shock]]

- **Gold**: [[Flaming]]

- **Platinum**: [[Frost]]

**Activate—Fling Coins** `pf2:2` (concentrate, manipulate)

**Effect** You whip the fortune cord, causing 10 coins loaded onto it to detach and fire at a creature within 100 feet that you can see. That creature takes 4d6 untyped damage (DC 28 [[Reflex]] save); the damage type depends on the type of coins you've loaded. Copper coins deal acid damage, silver coins deal electricity damage, gold coins deal fire damage, and platinum coins deal cold damage.

**Source:** `= this.source` (`= this.source-type`)
