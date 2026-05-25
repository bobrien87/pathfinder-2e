---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rhu-Chalik"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Greater Darkvision]], [[Tremorsense]] (precise) 60 feet"
languages: "Aklo (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +13, Deception +13, Diplomacy +13, Intimidation +13, Stealth +15"
abilityMods: ["+3", "+3", "+4", "+2", "+5", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Thoughtsense 60 feet"
    desc: "The rhu-chalik senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
  - name: "Excruciating Enzyme"
    desc: "A rhu-chalik's tendrils secrete an enzyme that causes intense pain. A living creature hit by a tendril Strike must succeed at a DC 24 [[Fortitude]] save or become [[Sickened]] 1 from the pain."
armorclass:
  - name: AC
    desc: "23 all-around vision; **Fort** +14, **Ref** +11, **Will** +17"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "No Breath"
    desc: "A rhu-chalik doesn't breathe and is immune to effects that require breathing (such as inhaled poisons)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +15 (`pf2:1`) (agile), **Damage** 2d4+6 bludgeoning plus 1d6 mental plus [[Excruciating Enzyme]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 24, attack +16<br>**5th** [[Mind Probe]]<br>**4th** [[Rewrite Memory]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Invisibility (At Will, Self Only)]]"
abilities_bot:
  - name: "Label Memories"
    desc: "`pf2:2` The rhu-chalik invades the mind of a target within 100 feet, sorting the memories into alien structures for transmission. The target must attempt a DC 24 [[Will]] save. <br> - **Critical Success** The target creature is unaffected and temporarily immune to Label Memories for 1 minute. <br> - **Success** The target is unaffected. <br> - **Failure** The target becomes [[Stupefied 2]] for 1 minute as its mind is reorganized to fit the rhu-chalik's needs. If it's already stupefied by this effect, the target instead becomes [[Confused]] for 1 minute or until it recovers due to taking damage. <br> - **Critical Failure** As failure, but if the target is already stupefied by Label Memories, they become [[Paralyzed]] for 1 minute instead of confused."
  - name: "Transmit Memories"
    desc: "`pf2:3` **Requirements** The rhu-chalik is adjacent to a creature [[Paralyzed]] due to Label Memories <br>  <br> **Effect** The rhu-chalik copies the creature's consciousness and mentally sends this copied consciousness through the void of space to their waiting masters. The target creature is deeply disoriented by this procedure, becoming [[Stupefied 2]] for 1 day afterward."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Also called void wanderers, rhu-chaliks can survive the depths of space indefinitely, passing between worlds over the eons and scouting those planets for the Dominion of the Black. Rhu-chaliks prefer to work alone in order to reduce potential overlap in their mental predations, but sometimes receive assistance from those who believe the transmission of memories is transcendent. The furtive beings are calculating and infinitely patient, seeking only the most exceptional minds to cast beyond the stars to their masters.

The Dominion of the Black is a conglomeration of deep-space conquerors with a strong presence on Aucturn, the most remote planet in Golarion's solar system. The Dominion has secret outposts all over Golarion; most of its members on the planet are scouts, using their skills to steal brains and identities, gathering information without any consideration for the inhabitants of the worlds they infiltrate.

```statblock
creature: "Rhu-Chalik"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
