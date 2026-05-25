---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Healing]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "expert in Medicine"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You firmly believe in the technique of strengthening one's life force, spiritual energies, and bodily fluids through the application of colored light. When using a torch, lantern, or other artificial light source to illuminate an area of dim light or darker, you use a combination of alchemical reagents, medicinal components, and colored lenses to turn that light one of seven colors, allowing you to help an ally recover from persistent damage. You give that target an assisted recovery, but the target can be anywhere within the bright light of the light source instead of needing to be adjacent to you. Ambient bright light (like sunlight) drowns out your artificial illumination and prevents you from using Chromotherapy.

The color of the light you choose determines the type of persistent damage from which you help the target recover.

ColorDescriptionRedYou increase blood flow to heat the body, attempting to end persistent cold damage.OrangeYou cancel out electric charge, attempting to end persistent electricity damage.YellowYou reduce pain and mental stress, attempting to end persistent mental damage.GreenYou promote blood flow in a way that helps clot wounds, attempting to end persistent bleed damage.BlueYou cool the body, attempting to end persistent fire damage.IndigoYou render acids inert, attempting to end persistent acid damage.VioletYou purify the body, attempting to end persistent poison damage.

**Source:** `= this.source` (`= this.source-type`)
