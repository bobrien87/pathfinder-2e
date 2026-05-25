---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Qarna"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +11, Intimidation +11, Nature +11, Religion +9, Stealth +10, Survival +11"
abilityMods: ["+3", "+4", "+3", "+1", "+3", "+1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "22 all-around vision; **Fort** +11, **Ref** +10, **Will** +11"
health:
  - name: HP
    desc: "65; **Immunities** fear effects; **Weaknesses** unholy 5"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 5 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +13 (`pf2:1`) (holy, magical, unarmed), **Damage** 1d8+9 piercing plus [[Push]]"
  - name: "Ranged strike"
    desc: "Composite Longbow +14 (`pf2:1`) (deadly d10, holy, magical, propulsive, volley 30, range 100 ft.), **Damage** 1d8+7 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +13<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Translocate]]<br>**2nd** [[Animal Messenger]]<br>**1st** [[Charm (Animals Only)]], [[Light]], [[Sure Strike]]"
abilities_bot:
  - name: "Archon's Pursuit"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Requirements** The qarna saw another creature teleport within the last round and has at least one [[Translocate]] spell remaining <br>  <br> **Effect** The qarna casts one of their *translocate* spells, which is heightened to 5th rank and causes the qarna to arrive in an unoccupied space it chooses within 30 feet of the creature it's pursuing. If the creature is too far away, the qarna arrives as close as possible."
  - name: "Distracting Arrow"
    desc: "`pf2:1` The qarna makes a composite longbow Strike. If it hits, the arrow lodges in the target and that creature's senses focus on the archon, leaving all else blurry. That creature takes a –2 status penalty to attack rolls and Perception checks against any target other than the qarna. The creature can Interact to remove the arrow, which ends the effect."
  - name: "Touch of Charity"
    desc: "`pf2:1` The qarna touches a willing living creature to take on that creature's wounds. The qarna transfers up to 30 of their own HP to the touched creature. (The qarna can't transfer more HP than they currently have.)"
  - name: "Push"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Qarnas are secretive and tireless sentinels and scouts, patrolling the Outer Sphere's untamed wilds for evil to eliminate and keeping small communities safe from demons, devils, and worse. They resemble ornate statuesque creations with four stag-like heads and golden horns. When requested to do so by their allies, especially the god Erastil, they journey into the Universe and patrol dangerous frontier areas, secretly performing acts of kindness such as leading hunters to food, helping lost children, and driving off evil creatures.

Archons are guardians of Heaven and enemies of corruption. Before gods and their servants set foot in the celestial planes, archons already resided in Heaven, the original inhabitants of the realm. Upon meeting, the archons and divine angels quickly discovered they were of a kind, holding justice and righteousness in their hearts. An alliance was formed, and archons now serve as stalwart allies to all celestials and mortals they find worthy.

While the first archons coalesced from the immense seven-tiered mountain of Heaven, they choose willing and worthy Heaven-bound souls to join their ranks. These mortals hear and answer the call of a mysterious voice, manifesting in the Garden at the mountain's peak. There they swear to forever serve the cause of justice and transform into their new archon forms.

Though deeply concerned with defending mortal life and willing to sacrifice themselves in battle against fiends, archons often feel rote and inscrutable to others, and their forms can border on frightening and bizarre. For this reason, they often have issues with interacting with mortals, or with the free spirited azatas. Despite this, archons draw great strength from others, especially those who exemplify virtue.

Beyond their celestial allies, archons also maintain ancient ties with aeons. The inscrutable factions can still be seen working together to defend longforgotten secrets and enforce rules that predate mortal life. Archons explain these missions as necessary without further elaboration, leaving even their angelic allies frustrated with archons' obstinance.

```statblock
creature: "Qarna"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
