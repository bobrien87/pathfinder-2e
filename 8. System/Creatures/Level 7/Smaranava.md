---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Smaranava"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +17, Arcana +16, Athletics +13, Deception +16, Intimidation +16, Stealth +19"
abilityMods: ["+2", "+6", "+4", "+3", "+2", "+3"]
abilities_top:
  - name: "Coils of Knowledge"
    desc: "The naga's grip is more spiritual than physical. A creature hit by a smaranava's tail must succeed at a DC 25 [[Will]] save or become [[Grabbed]] by the tail until they [[Escape]], the naga releases them with an Interact action, or the naga dies. <br>  <br> A captive takes a –4 status penalty to Escape, but can choose to attempt an Occultism or Religion check to Escape instead of the usual options without taking this penalty"
  - name: "Smaranava Venom"
    desc: "When a holy creature succeeds at a saving throw against this poison, it is immediately cured <br>  <br> **Saving Throw** DC 25 [[Will]] save <br>  <br> **Maximum Duration** 5 minutes <br>  <br> **Stage 1** [[Slowed]] 1 (1 round) <br>  <br> **Stage 2** [[Slowed]] 2 (1 round) <br>  <br> **Stage 3** [[Unconscious]] with no Perception check to wake up (1 minute)"
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "115"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +20 (`pf2:1`) (finesse, magical), **Damage** 2d10+5 piercing plus [[Smaranava Venom]]"
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (agile, finesse, magical, reach 15 ft.), **Damage** 2d8+5 bludgeoning plus [[Coils Of Knowledge]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17<br>**3rd** [[Lightning Bolt]], [[Mind Reading]]<br>**2nd** [[Dispel Magic]]<br>**1st** [[Detect Magic]], [[Read Aura]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d8+5)[bludgeoning]], DC 25 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Many view clouded nagas as jealous, malevolent creatures. Only those with the courage to see clearly can recognize these beings for what they truly are: tragic, wounded beings who have been trapped and corrupted by fate. The betrayal and beheading of the naga's mother goddess, Ravithra, cascaded trauma onto all of her creations. Smaranavas have never recovered from this divine wound, and these cursed serpents live wretched half-lives, attempting to fulfill Ravithra's forgotten purpose by tempting and testing mortals they encounter. In this way, they separate the wicked from the righteous, the worthy from the unworthy.

Smaranavas have dark scales that are rendered dull gray by stuck shed skin, their eyes a milky white due to opaque caps over their eyes. Many ritually scar their necks out of sorrow for their mother Ravithra. Legends claim that the wise and enlightened can free clouded naga from their fates, allowing them to shed their forms and emerge as an awakener naga.

Nagas are serpentine beings with magical powers and keen intellects. Physically, they resemble massive snakes, though they often wear jewelry and other ornaments that clearly separate them from their animal kin. Nagas use their innate magic and poisonous fangs to keep all but the most stalwart foes at bay. They keep their own counsel, viewing their cosmic role to be sacrosanct and beyond the understanding of outside scholars. Their unwillingness to explain themselves or entertain the suggestion of alliances has led to a long history of conflict with their neighbors, who read them as aloof, arrogant, or duplicitous.

Nagas often have a powerful sense of duty to their perceived role within the universe, even if this role leads them to violent or tragic ends. Many see them as harsh and stern due to their devotion, terrifying in their majesty yet possessed of an aura of transcendence.

```statblock
creature: "Smaranava"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
