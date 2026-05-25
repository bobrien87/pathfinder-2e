---
type: creature
group: ["Clockwork", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Clockwork Soldier"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15"
abilityMods: ["+6", "+2", "+4", "-5", "+4", "-5"]
abilities_top:
  - name: "+2 vs. Disarm"
    desc: ""
  - name: "Wind-Up"
    desc: "24 hours, DC 22 Thievery, standby <br>  <br> For a clockwork to act, it must be wound with a unique key by another creature. This takes 1 minute. Once wound, it remains operational for the listed amount of time, usually 24 hours, after which time it becomes unaware of its surroundings and can't act until it's wound again. Some clockworks' abilities require them to spend some of their remaining operational time. They can't spend more than they have and shut down immediately once they have 0 time remaining. If it's unclear when a clockwork was last wound, most clockwork keepers wind all their clockworks at a set time, typically 8 a.m. <br>  <br> A clockwork that lists standby in its wind-up entry can enter standby mode as a 3-action activity. Its operational time doesn't decrease in standby, but it can sense its surroundings (with a -2 penalty to Perception). It can't act, with one exception: when it perceives a creature, it can exit standby as a reaction (rolling initiative if appropriate). <br>  <br> A creature can attempt to [[Disable a Device]] to wind a clockwork down (with a DC listed in the wind-up entry). For each success, the clockwork loses 1 hour of operational time. This can be done even if the clockwork is in standby mode."
armorclass:
  - name: AC
    desc: "24; **Fort** +16, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "80; **Weaknesses** electricity 5, orichalcum 5; **Resistances** physical 5 except adamantine, orichalcum"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Halberd +17 (`pf2:1`) (magical, reach 10 ft., versatile s), **Damage** 1d10+10 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, unarmed), **Damage** 1d8+10 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Activate Defenses"
    desc: "`pf2:1` One of the soldier's external plates extends on a mechanical actuator to defend the soldier or an adjacent creature of the soldier's choice. <br>  <br> The creature gains a +2 circumstance bonus to AC until the start of the soldier's next turn, or until it is no longer adjacent to the soldier, whichever comes first. The soldier can have no more than one plate extended at a time. <br>  <br> > [!danger] Effect: Activate Defenses"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These diligent machines guard their assigned posts tirelessly. A typical clockwork soldier stands 6 feet tall and consists of 500 pounds of metal and magic.

Intricate, complex machines, clockworks are built with care by highly skilled engineers. Though their creation involves some amount of magic, they're primarily mechanical, packed with precision-tuned gears and springs working in concert.

The sturdy mainspring within a clockwork must be wound to provide the energy needed to power the device. Some larger clockworks contain a series of springs for different limbs that each need to be wound. A clockwork's crafter creates a unique metal key while building the clockwork; winding the clockwork usually involves inserting the key into the machine's back and turning clockwise. Larger clockworks require greater strength to turn the key, and typically have larger keys to allow for more torque-some even accommodating a team of winders rather than an individual. Programming a clockwork requires both the key and the knowledge to set the program correctly, information usually reserved for the clockwork's creator or owner.

```statblock
creature: "Clockwork Soldier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
