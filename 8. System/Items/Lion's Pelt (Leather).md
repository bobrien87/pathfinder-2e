---
type: item
source-type: "Remaster"
level: "6"
price: "{'gp': 250}"
bulk: "1"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** You're a member of the Lion Blades.

Laurisa Tromaine ordered these as prototype uniforms. The fur-lined pauldrons bear the insignia of a lion with a blade in its mouth. The type of blade indicates which bard school one graduated from. When you disguise the armor via its [[Raiment]] rune, you can choose whether to conceal this symbol or not. You can also use the rune's activation to quickly display or hide the insignia.

**Activate—Contact Ally** `pf2:1` (arcane, concentrate)

**Frequency** once per hour

**Effect** You cast [[Message]] at 1st rank to a target that you know is also wearing a *lion's pelt* uniform. If you and the target share an insignia, the spell is heightened to 3rd rank.

**Source:** `= this.source` (`= this.source-type`)
