---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Light]]", "[[Magical]]"]
price: "{'gp': 1850}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted from cold iron, this black hooded lantern has gray glass and lenses that emit a pale gray light when the lantern is lit. Anything this light falls on looks gray or desaturated. The lantern uses oil as a standard hooded lantern. The lantern's light shines within the Ethereal Plane as well as the Universe. On any other plane, the light functions as a normal hooded lantern.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Requirements** The lantern's shutters are open

**Effect** You concentrate on the lantern's light to soften the boundary between the Ethereal Plane and the Universe. Any creature in the lantern's bright light on the Universe gains the effects of the [[Ghost Touch]] property rune on all its weapons and unarmed attacks. If an affected weapon or attack is magical and already has the maximum number of property runes, the wielder can choose one to suppress to gain ghost touch. This benefit lasts for 5 minutes or until the shutters are closed, whichever comes first. It applies to a creature only while it's in the lantern's bright light, and if the creature leaves the light and returns it regains the benefit once more.

**Source:** `= this.source` (`= this.source-type`)
