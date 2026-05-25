---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Structure]]"]
price: "{'gp': 1300}"
usage: "other"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While many of the magical wonders created by saumen kar have been destroyed, *ice forges*, while rare, still see use today among the few individuals who manage to discover and keep one of these portable treasures. When an *ice forge* isn't activated, it appears to be a small anvil carved from a lump of ice no larger than an apple. While in this state, the *ice forge* remains cold to the touch but doesn't melt in the presence of high temperatures. It can be used to chill a beverage in a small container, although those who venerate and respect these items' legacy would doubtless find this use to be insulting at best.

**Activate—Expand Forge** `pf2:3` (concentrate, manipulate)

**Effect** You toss the *ice forge* onto the ground, and it immediately expands in size, transforming into a fully functional forge that appears to be made of solid ice. Expanded, the *ice forge* is 10 feet square and 10 feet high. While the forge itself is cold to the touch, it won't melt in higher temperatures, nor will it cause harm to someone who remains in contact with the chill surface for an extended period of time. The forge can be used to work metal as a normal forge (although fuel must be provided)—the heat created by its use does no harm to the *ice forge*, nor does it transmit to the surface it sits upon, making an *ice forge* an ideal solution for those who seek to use forges in areas where open flames or smoke would be dangerous.

You can return an *ice forge* to its handheld anvil form by spending a single action to issue a verbal command, which has the auditory trait. Doing so immediately snuffs out any fire within the forge and leaves behind unused material or ashes. Once deactivated, the forge can't be activated again for 4 hours.

**Activate—Ice Sculpture** 1 minute (concentrate, manipulate)

**Requirements** The *ice forge* is in forge form

**Frequency** once per day

**Effect** The *ice forge* casts [[Creation]] (heightened to 5th rank) to your specifications.

**Source:** `= this.source` (`= this.source-type`)
