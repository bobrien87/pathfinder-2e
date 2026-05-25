---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Extradimensional]]", "[[Magical]]"]
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

A complex, collapsible mechanism forms the outer surface of a planar tunnel. It's linked to a passageway that can be accessed if the tunnel is fully opened. The passage is extradimensional, but borders another plane of existence. Each planar tunnel is keyed to one specific plane. If another extradimensional space is opened inside the planar tunnel, rather than deactivating either item as typical for extradimensional spaces, a rift to the keyed plane tears open and destroys both items. Any creature or unattended object in the planar tunnel is instantly transported to the keyed plane, though a creature can avoid this by succeeding at a DC 30 [[Reflex]] save.

**Activate** `pf2:3` (manipulate)

You open the collapsed mechanism to fully open the tunnel, revealing an extradimensional space that stays in place. The tunnel is 6 feet across—just big enough to cover a 5-foot square—and 10 feet deep. The passage's depth is perpendicular to the surface, so it's most commonly placed on a floor to make a hole straight down or on a wall to create a horizontal passage through it. The atmosphere is hospitable to travel even if the keyed plane wouldn't be. Anyone adjacent to either edge of the tunnel can Interact to collapse the opening. This closes both entrances to the extradimensional space. Any objects or creatures within the tunnel remain inside, and any that can't fit fully inside are ejected into the nearest open space. No matter how many items are in the planar tunnel, its Bulk never changes. Items can be stowed or retrieved only while the tunnel is fully open. When the tunnel is closed, the interior remains a stable environment for 10 minutes, after which any creature or object inside is subjected to the environment of the keyed plane as it seeps through the boundary. A living creature placed inside can attempt to [[Escape]] against a DC of 13. An item inside the tunnel provides no benefits unless it's retrieved first. Anything in the tunnel can't be detected by magic that detects only things on the same plane.

**Special** A planar tunnel can be used as a planar key for the [[Interplanar Teleport]] spell, and has the same rarity as the key, as specified in the spell.

**Source:** `= this.source` (`= this.source-type`)
