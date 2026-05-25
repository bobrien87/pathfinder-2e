---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "worn"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This pristine leather belt is made of treated and polished black leather with silver fittings; it features a pair of matching leather holsters that can each fit a one-handed firearm or hand crossbow.

**Activate—Immaculatize** `pf2:3` (concentrate)

**Frequency** once per day

**Effect** Up to two firearms currently holstered in the immaculate holsters are instantly cleaned and oiled, protecting them from accidental misfires (though not misfires caused as a result of using a feat or ability). The holstered weapons are also reloaded with non-magical 0-level ammunition appropriate to a weapon of their type; if a firearm has multiple chambers, such as a slide pistol, each empty chamber is loaded. Immaculate holsters can't reload the cartridge of a repeating weapon.

**Source:** `= this.source` (`= this.source-type`)
