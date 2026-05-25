---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Okenevem"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Diplomacy +28, Medicine +28, Nature +28, Religion +31, Society +27, Heaven Lore +33"
abilityMods: ["+4", "+6", "+5", "+6", "+8", "+7"]
abilities_top:
  - name: "Humble Bow"
    desc: "A creature hit by one of the okenevem's Strikes is compelled to bow down in reverence. It must succeed at a DC 36 [[Will]] save or fall [[Prone]]. If the creature Stands before the end of its next turn, it takes 3d8 mental damage. If the creature succeeds, it's temporarily immune for 1 minute."
armorclass:
  - name: AC
    desc: "35; **Fort** +25, **Ref** +26, **Will** +31"
health:
  - name: HP
    desc: "250; **Immunities** fear effects; **Weaknesses** unholy 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy. <br>  <br> > [!danger] Effect: Archon's Protection"
  - name: "Divine Defenders"
    desc: "60 feet. Okenevem hold an exalted place among archons for their holy station. This draws lesser archons to defend them. When an enemy in the aura takes a hostile action against the okenevem, a cloud of minor archons swarms around it, causing it to take @Damage[2d6[persistent,slashing],2d6[persistent,spirit]]{2d6 persistent slashing damage and 2d6 persistent spirit damage}. This persistent damage ends automatically if the enemy spends a round without taking a hostile action against the okenevem."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Humbling Touch +29 (`pf2:1`) (divine, finesse, holy, mental, nonlethal, spirit), **Damage** 4d6 spirit plus 4d8 mental plus [[Humble Bow]]"
  - name: "Ranged strike"
    desc: "Humbling Word +27 (`pf2:1`) (auditory, divine, holy, mental, nonlethal, spirit, range 60 ft.), **Damage** 4d8 mental plus 4d6 spirit plus [[Humble Bow]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28<br>**5th** [[Spiritual Guardian]], [[Truespeech]] (Constant)<br>**4th** [[Translocate]] (At Will)<br>**2nd** [[Calm]]<br>**1st** [[Divine Lance]], [[Light]], [[Message]]"
abilities_bot:
  - name: "Sublime Vision"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The okenevem casts the [[Overwhelming Presence]] spell, except instead of aggrandizing themself, the okenevem summons a vision of Heaven within 100 feet, and the target must humble themself in self-refection rather than pay tribute."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The most powerful archons reside in Iudica, the sixth tier on the holy mountain of Heaven. Okenevems live among their number. Okenevems have evolved from lowly zoaems to their current form, but they possess even further potential—the grace to pass through into the Garden at the pinnacle of Heaven. Yet these archons choose not to, instead prostrating themselves at its gates, at peace with never entering. Humble and unpretentious above all, they bow before the grandeur of Heaven and set themselves to work in other ways.

Okenevems rarely travel away from Heaven unless they're tasked with a specifc deed by the divinities of that plane. Most of these missions require okenevems to bring humility to priests who press against the will of deities, defy the order of heaven, or consider themselves to be of equal power to their god. They seek to steer these priests away from the dangers of such arrogance, often by example.

```statblock
creature: "Okenevem"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
