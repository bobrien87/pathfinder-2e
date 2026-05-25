---
type: item
source-type: "Remaster"
level: "5"
price: "{'gp': 150}"
usage: "held-in-two-hands"
bulk: "16"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Etheric spirit-singers create an eerie spectral sound based on the presence of spiritual essence and other ethereal energies. All spirit-singers can be used as musical instruments by manipulating the sensitivity to ethereal energies. However, they have an even greater benefit in areas heavy with spiritual essence. When played in the presence of a significant spiritual disturbance, such as a haunt or an incorporeal undead, a spirit-singer grants you a +1 item bonus to Performance checks. While playing a spirit-singer, you also gain a +1 item bonus to checks to detect a haunt or incorporeal undead, and you can roll a check to notice a haunt even if you aren't actively Searching for it, due to the distortions of the spirit-singer's music. A haunt or incorporeal undead that is intelligent enough to notice the effects it is having on the spirit-singer's music and that can't otherwise communicate with the living might choose to use the spirit-singer to do so if it wishes. For instance, it could try to guide the spirit-singer player towards a location by creating distortions in that direction or, if it understands language, it could try to answer questions by creating one distortion for yes and two distortions for no. Unless stated otherwise in its usage entry, a spirit-singer functions like a heavy musical instrument; rather than carrying it, the musician places the spirit-singer in a particular position and uses both hands to play.

**Source:** `= this.source` (`= this.source-type`)
