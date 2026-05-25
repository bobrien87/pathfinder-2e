---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 6000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Several small charms shaped like weapons hang from an *armory bracelet*, which is often brass. The bracelet has one charm each for the groups axe, bow, brawling, club, crossbow, dart, flail, hammer, knife, pick, polearm, shield, sling, spear, and sword. Uncommon and rare versions of the bracelet might include charms for firearms or create uncommon weapons.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You pull one charm from the bracelet. The charm transforms into a common weapon of your choice from the charm's weapon group. If the weapon requires ammunition, it appears with a quiver or pouch with 20 pieces of ammunition for the weapon. The weapon is a *+3 greater striking weapon* of the type you chose. After 1 minute, the weapon transforms into a *+2 greater striking* weapon and remains until your next daily preparations. At that point, the weapon and any remaining ammunition crumble to dust and all the charms reappear on the bracelet. The weapon and ammunition created with the charm are noticeably different from others and can't be sold.

**Source:** `= this.source` (`= this.source-type`)
