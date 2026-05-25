---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rekhep"
level: "10"
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
    desc: "+19; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean, Utopian (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +21, Diplomacy +19, Intimidation +19, Religion +19, Survival +17"
abilityMods: ["+5", "+1", "+7", "+2", "+3", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Courageous Switch"
    desc: "When a rekhep uses their [[Translocate]] innate spell, they can choose to move into the space of a willing ally they can see within range. If they do, the ally switches places with the archon, appearing in the space the archon just vacated, as if it too had cast *translocate*."
  - name: "Holy Armament"
    desc: "Any weapon gains the *[[Holy]]* rune while the rekhep wields it."
armorclass:
  - name: AC
    desc: "31 all-around vision; **Fort** +23, **Ref** +15, **Will** +19"
health:
  - name: HP
    desc: "150; **Immunities** fear effects; **Weaknesses** unholy 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 15 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Holy Lance +22 (`pf2:1`) (deadly d8, divine, holy, jousting d6, reach 10 ft.), **Damage** 2d8+11 piercing plus 1d4 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 27, attack +19<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Translocate]] (At Will)<br>**2nd** [[Share Life]]<br>**1st** [[Divine Lance]], [[Message]], [[Sure Strike]]"
abilities_bot:
  - name: "Archon's Pursuit"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Requirements** The rekhep saw another creature teleport within the last round and has at least one [[Translocate]] spell remaining <br>  <br> **Effect** The rekhep casts one of their *translocate* spells, which is heightened to 5th rank and causes the qarna to arrive in an unoccupied space it chooses within 30 feet of the creature it's pursuing. If the creature is too far away, the rekhep arrives as close as possible."
  - name: "Living Shield"
    desc: "`pf2:1` The rekhep grants an adjacent ally a +2 circumstance bonus to AC until they're no longer adjacent or until the start of the archon's next turn, whichever comes first. When the rekhep uses Archon's Protection against an attack against the shielded ally, the rekhep gains the resistance and takes the damage rather than the ally. <br>  <br> > [!danger] Effect: Living Shield"
  - name: "Terrifying Smite"
    desc: "`pf2:2` The rekhep makes a Strike against an enemy that has one of the rekhep's allies within its reach. On a hit, the target takes an additional 2d8 mental damage and is [[Frightened]] 2. The extra damage and frightened value are doubled on a critical hit."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Rekheps are the living shields that defend Heaven against fiendish incursions. They tile together in massive formations capable of withstanding any onslaught. Given their tremendous strength and imposing stature, shield archons are ideal guardians of the meek and are sometimes summoned to the mortal Universe to ward off the attacks of great numbers of evildoers.

Archons are guardians of Heaven and enemies of corruption. Before gods and their servants set foot in the celestial planes, archons already resided in Heaven, the original inhabitants of the realm. Upon meeting, the archons and divine angels quickly discovered they were of a kind, holding justice and righteousness in their hearts. An alliance was formed, and archons now serve as stalwart allies to all celestials and mortals they find worthy.

While the first archons coalesced from the immense seven-tiered mountain of Heaven, they choose willing and worthy Heaven-bound souls to join their ranks. These mortals hear and answer the call of a mysterious voice, manifesting in the Garden at the mountain's peak. There they swear to forever serve the cause of justice and transform into their new archon forms.

Though deeply concerned with defending mortal life and willing to sacrifice themselves in battle against fiends, archons often feel rote and inscrutable to others, and their forms can border on frightening and bizarre. For this reason, they often have issues with interacting with mortals, or with the free spirited azatas. Despite this, archons draw great strength from others, especially those who exemplify virtue.

Beyond their celestial allies, archons also maintain ancient ties with aeons. The inscrutable factions can still be seen working together to defend longforgotten secrets and enforce rules that predate mortal life. Archons explain these missions as necessary without further elaboration, leaving even their angelic allies frustrated with archons' obstinance.

```statblock
creature: "Rekhep"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
